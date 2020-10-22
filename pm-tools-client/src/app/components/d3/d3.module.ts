import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeatmapComponent } from './heatmap/heatmap.component';


@NgModule({
  declarations: [HeatmapComponent],
  imports: [
    CommonModule
  ],
  exports: [HeatmapComponent]
})
export class D3Module { }
