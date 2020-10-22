import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { PortfoliosPageRoutingModule } from './model-portfolios-routing.module';

import { ModelPortfoliosPage } from './model-portfolios.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    PortfoliosPageRoutingModule
  ],
  declarations: [ModelPortfoliosPage]
})
export class ModelPortfoliosPageModule {}
