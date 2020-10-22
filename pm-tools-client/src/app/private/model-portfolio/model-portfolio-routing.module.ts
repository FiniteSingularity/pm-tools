import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ModelPortfolioPage } from './model-portfolio.page';

const routes: Routes = [
  {
    path: '',
    component: ModelPortfolioPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ModelPortfolioPageRoutingModule {}
