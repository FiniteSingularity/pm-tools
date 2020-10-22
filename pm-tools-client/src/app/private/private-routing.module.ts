import { RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

const routes = [
  {
    path: 'dashboard',
    loadChildren: () =>
      import('./dashboard/dashboard.module').then((m) => m.DashboardPageModule),
  },
  {
    path: 'model-portfolios',
    loadChildren: () => import('./model-portfolios/model-portfolios.module').then( m => m.ModelPortfoliosPageModule)
  },
  {
    path: 'model-portfolios/:id',
    loadChildren: () => import('./model-portfolio/model-portfolio.module').then( m => m.ModelPortfolioPageModule)
  },
];

@NgModule({
  declarations: [],
  exports: [RouterModule],
  imports: [RouterModule.forChild(routes)],
})
export class PrivateRoutingModule {}
