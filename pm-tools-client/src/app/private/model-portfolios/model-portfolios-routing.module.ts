import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ModelPortfoliosPage } from './model-portfolios.page';

const routes: Routes = [
  {
    path: '',
    component: ModelPortfoliosPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class PortfoliosPageRoutingModule {}
