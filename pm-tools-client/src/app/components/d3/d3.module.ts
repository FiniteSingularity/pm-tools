import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeatmapComponent } from './heatmap/heatmap.component';
import { FrontierPlotComponent } from './frontier-plot/frontier-plot.component';


@NgModule({
  declarations: [HeatmapComponent, FrontierPlotComponent],
  imports: [
    CommonModule
  ],
  exports: [HeatmapComponent, FrontierPlotComponent]
})
export class D3Module { }
