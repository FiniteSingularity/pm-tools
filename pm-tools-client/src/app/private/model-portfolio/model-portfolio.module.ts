import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { ModelPortfolioPageRoutingModule } from './model-portfolio-routing.module';

import { ModelPortfolioPage } from './model-portfolio.page';
import { D3Module } from '@components/d3/d3.module';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    D3Module,
    ModelPortfolioPageRoutingModule
  ],
  declarations: [ModelPortfolioPage]
})
export class ModelPortfolioPageModule {}
