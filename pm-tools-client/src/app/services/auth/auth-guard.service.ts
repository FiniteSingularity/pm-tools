import { Injectable } from '@angular/core';
import {
  CanActivate,
  Router,
  ActivatedRouteSnapshot,
  RouterStateSnapshot,
} from '@angular/router';
import { AuthenticationService } from './authentication.service';

@Injectable({
  providedIn: 'root',
})
export class AuthGuardService implements CanActivate {
  constructor(
    private authService: AuthenticationService,
    private router: Router
  ) {}

  async canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): Promise<boolean> {
    const authStatus = await this.authService.authenticationStatus();

    if (authStatus.authenticated) {
      if (authStatus.firstLogin && state.url !== '/private/first-login') {
        this.router.navigate(['/private/first-login']);
      }
      return true;
    }
    this.router.navigate(['/login']);
    return false;
  }
}
