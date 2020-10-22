import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { PortfoliosPageRoutingModule } from './portfolios-routing.module';

import { PortfoliosPage } from './portfolios.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    PortfoliosPageRoutingModule
  ],
  declarations: [PortfoliosPage]
})
export class PortfoliosPageModule {}
