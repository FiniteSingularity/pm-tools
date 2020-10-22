import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';
import { AuthGuardService } from '@services/auth/auth-guard.service';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'private/dashboard',
    pathMatch: 'full'
  },
  {
    path: 'public',
    loadChildren: () =>
      import('./public/public-routing.module').then((m) => m.PublicRoutingModule),
  },
  {
    path: 'private',
    loadChildren: () =>
      import('./private/private-routing.module').then((m) => m.PrivateRoutingModule),
    canActivate: [AuthGuardService]
  }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule {}
