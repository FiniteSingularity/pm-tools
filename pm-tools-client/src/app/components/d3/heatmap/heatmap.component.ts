import { Component, Input, OnInit } from '@angular/core';
import { CorrelationMatrixEntry } from '@app/models/portfolio.models';
import * as d3 from 'd3';

@Component({
  selector: 'app-heatmap',
  templateUrl: './heatmap.component.html',
  styleUrls: ['./heatmap.component.scss'],
})
export class HeatmapComponent implements OnInit {
  @Input() data: CorrelationMatrixEntry[];
  @Input() tickers: string[];
  private svg;
  private margin = 50;
  private width = 500 - (this.margin * 2);
  private height = 500 - (this.margin * 2);

  constructor() { }

  ngOnInit() {
    this.createSvg();
    this.createHeatmap();
  }

  private createSvg(): void {
      this.svg = d3.select("figure#heatmap")
        .append("svg")
        .attr("width", this.width + (this.margin * 2))
        .attr("height", this.height + (this.margin * 2))
        .append("g")
        .attr("transform", "translate(" + this.margin + "," + this.margin + ")");
  }

  private createHeatmap() {
    // Build X scales and axis:
    const x = d3.scaleBand()
      .range([ 0, this.width ])
      .domain(this.tickers)
      .padding(0.05);
    this.svg.append("g")
      .style("font-size", 15)
      .attr("transform", "translate(0," + this.height + ")")
      .call(d3.axisBottom(x).tickSize(0))
      .selectAll("text")
      .attr("transform", "translate(10, 15)rotate(45)")
      .select(".domain").remove()
      

    // Build Y scales and axis:
    const y = d3.scaleBand()
      .range([ this.height, 0 ])
      .domain(this.tickers.reverse())
      .padding(0.05);
    this.svg.append("g")
      .style("font-size", 15)
      .call(d3.axisLeft(y).tickSize(0))
      .select(".domain").remove()

    // Build color scale
    const myColor = d3.scaleSequential()
      .interpolator(d3.interpolateRdBu)
      .domain([1,-1])

    // create a tooltip
    const tooltip = d3.select("#tooltip-holder")
      .append("div")
      .style("opacity", 0)
      .attr("class", "tooltip")
      .style("background-color", "white")
      .style("border", "solid")
      .style("border-width", "2px")
      .style("border-radius", "5px")
      .style("padding", "5px")

    // Three function that change the tooltip when user hover / move / leave a cell
    const mouseover = function(d) {
      tooltip
        .style("opacity", 1)
      d3.select(this)
        .style("stroke", "black")
        .style("opacity", 1)
    }
    const mousemove = function(d) {
      tooltip
        .html(`${d.t2}-${d.t1}: ${d.value.toFixed(2)}`)
        .style("left", (d3.mouse(this)[0]+70) + "px")
        .style("top", (d3.mouse(this)[1]) + "px")
    }
    const mouseleave = function(d) {
      tooltip
        .style("opacity", 0)
      d3.select(this)
        .style("stroke", "none")
        .style("opacity", 0.8)
    }

    // add the squares
    this.svg.selectAll()
      .data(this.data, function(d) {return d.t1+':'+d.t2;})
      .enter()
      .append("rect")
        .attr("x", function(d) { return x(d.t1) })
        .attr("y", function(d) { return y(d.t2) })
        .attr("rx", 4)
        .attr("ry", 4)
        .attr("width", x.bandwidth() )
        .attr("height", y.bandwidth() )
        .style("fill", function(d) { return myColor(d.value)} )
        .style("stroke-width", 4)
        .style("stroke", "none")
        .style("opacity", 0.8)
      .on("mouseover", mouseover)
      .on("mousemove", mousemove)
      .on("mouseleave", mouseleave)

    // // Add title to graph
    // this.svg.append("text")
    //         .attr("x", 0)
    //         .attr("y", -50)
    //         .attr("text-anchor", "left")
    //         .style("font-size", "22px")
    //         .text("A d3.js heatmap");

    // // Add subtitle to graph
    // this.svg.append("text")
    //         .attr("x", 0)
    //         .attr("y", -20)
    //         .attr("text-anchor", "left")
    //         .style("font-size", "14px")
    //         .style("fill", "grey")
    //         .style("max-width", 400)
    //         .text("A short description of the take-away message of this chart.");
  }
}
