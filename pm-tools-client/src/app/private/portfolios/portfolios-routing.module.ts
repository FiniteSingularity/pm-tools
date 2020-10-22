import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PortfoliosPage } from './portfolios.page';

const routes: Routes = [
  {
    path: '',
    component: PortfoliosPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class PortfoliosPageRoutingModule {}
