import { Router } from '@angular/router';
import { map, catchError } from 'rxjs/operators';
import { AuthenticationService } from '../auth/authentication.service';
import { Injectable, OnDestroy } from '@angular/core';
import { Subscription, Observable, empty, EMPTY, throwError } from 'rxjs';
import {
  HttpInterceptor,
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpResponse,
  HttpErrorResponse,
} from '@angular/common/http';
import { snakecaseKeys, camelizeKeys } from '@shared/utils/camelize';

@Injectable({
  providedIn: 'root',
})
export class ApiInterceptorService implements HttpInterceptor, OnDestroy {
  authSub: Subscription;
  token: string = null;

  constructor(
    private authService: AuthenticationService,
    private router: Router
  ) {
    this.authSub = this.authService.authenticationState.subscribe(authDat => {
      this.token = authDat.token ? authDat.token : authDat.token;
    });
  }

  ngOnDestroy() {
    this.authSub.unsubscribe();
  }

  intercept(
    request: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {
    // TODO: This is hacky.  Fix it!
    if (!this.token) {
      this.token = this.authService.token;
    }
    if (this.token) {
      request = request.clone({
        setHeaders: {
          Authorization: `Token ${this.token}`,
        },
      });
    } else {
      console.log('No token!');
    }
    const reqBodySnake = snakecaseKeys(request.body);
    request = request.clone({ body: reqBodySnake });

    return next.handle(request).pipe(
      map((event: HttpEvent<any>) => {
        if (event instanceof HttpResponse) {
          const camelCaseObject = camelizeKeys(event.body);
          const modEvent = event.clone({ body: camelCaseObject });
          return modEvent;
        } else {
          return event;
        }
      }),
      catchError((err, caught) => {
        if (err instanceof HttpErrorResponse) {
          if (err.status === 403) {
            // redirect to the login route
            // or show a modal
            this.authService.logout().then(() => {
              window.location.reload();
            });
            return EMPTY;
          } else if (err.status === 400) {
            return throwError(err);
          }
        }
        return EMPTY;
      })
    );
  }
}
