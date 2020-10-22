import { Component, OnInit } from '@angular/core';
import * as d3 from 'd3';

interface axisRange {
  min: number;
  max: number;
}

@Component({
  selector: 'app-frontier-plot',
  templateUrl: './frontier-plot.component.html',
  styleUrls: ['./frontier-plot.component.scss'],
})
export class FrontierPlotComponent implements OnInit {
  holdings = [
    {ticker: 'AAPL', sigma: 0.28, er: 0.14},
    {ticker: 'GE', sigma: 0.22, er: 0.10}
  ]

  frontier = [
    {sigma: 0.03, er: 0.04},
    {sigma: 0.04, er: 0.06},
    {sigma: 0.05, er: 0.07},
  ]

  private svg;
  private margin = 50;
  private width = 500 - (this.margin * 2);
  private height = 500 - (this.margin * 2);
  private xRange: axisRange = {min: 999, max: -999};
  private yRange: axisRange = {min: 999, max: -999};

  constructor() { }

  ngOnInit() {
    this.calcRanges();
    this.createSvg();
    this.createFrontierPlot();
  }

  private calcRanges() {
    this.holdings.forEach(holding => {
      this.xRange.min = Math.min(this.xRange.min, holding.sigma);
      this.xRange.max = Math.max(this.xRange.max, holding.sigma);
      this.yRange.min = Math.min(this.yRange.min, holding.er);
      this.yRange.max = Math.max(this.yRange.max, holding.er);
    });
    this.frontier.forEach(point => {
      this.xRange.min = Math.min(this.xRange.min, point.sigma);
      this.xRange.max = Math.max(this.xRange.max, point.sigma);
      this.yRange.min = Math.min(this.yRange.min, point.er);
      this.yRange.max = Math.max(this.yRange.max, point.er);
    })
  }

  private createSvg(): void {
    this.svg = d3.select("figure#heatmap")
      .append("svg")
      .attr("width", this.width + (this.margin * 2))
      .attr("height", this.height + (this.margin * 2))
      .append("g")
      .attr("transform", "translate(" + this.margin + "," + this.margin + ")");
  }


  private createFrontierPlot() {
    this.svg
      .append("rect")
      .attr("x",0)
      .attr("y",0)
      .attr("height", this.height)
      .attr("width", this.height)
      .style("fill", "EBEBEB")
  }
}
