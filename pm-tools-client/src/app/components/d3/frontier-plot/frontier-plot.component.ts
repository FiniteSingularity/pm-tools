import { Component, Input, OnInit } from '@angular/core';
import * as d3 from 'd3';

interface axisRange {
  min: number;
  max: number;
}

interface point {
  ticker?: string;
  sigma: number;
  er: number;
}

@Component({
  selector: 'app-frontier-plot',
  templateUrl: './frontier-plot.component.html',
  styleUrls: ['./frontier-plot.component.scss'],
})
export class FrontierPlotComponent implements OnInit {
  @Input() holdings: point[];
  @Input() frontier: point[];

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
    
    // Add X axis
    const x = d3.scaleLinear()
      .domain([this.xRange.min*0.95, this.xRange.max*1.05])
      .range([ 0, this.width ])
    this.svg.append("g")
      .attr("transform", "translate(0," + this.height + ")")
      .call(d3.axisBottom(x).tickSize(-this.height).ticks(10))
      .select(".domain").remove()

    // Add Y axis
    const y = d3.scaleLinear()
      .domain([this.yRange.min*0.95, this.yRange.max*1.05])
      .range([ this.height, 0])
      .nice()
    this.svg.append("g")
      .call(d3.axisLeft(y).tickSize(-this.width).ticks(7))
      .select(".domain").remove()

    // create a tooltip
    const HoldingToolTip = d3.select("#tooltip-holder")
      .append("div")
      .style("opacity", 0)
      .attr("class", "tooltip")
      .style("background-color", "white")
      .style("border", "solid")
      .style("border-width", "2px")
      .style("border-radius", "5px")
      .style("padding", "5px")

      // Three function that change the tooltip when user hover / move / leave a cell
      const holdingMouseover = function(d) {
        HoldingToolTip
          .style("opacity", 1)
      }
      var holdingMousemove = function(d) {
        HoldingToolTip
          .html(`${d.ticker}- &sigma;: ${d.sigma}, er:${d.er} `)
          .style("left", (d3.mouse(this)[0]+70) + "px")
          .style("top", (d3.mouse(this)[1]) + "px")
      }
      var holdingMouseleave = function(d) {
        HoldingToolTip
          .style("opacity", 0)
      }

    // Customization
    this.svg.selectAll(".tick line").attr("stroke", "white")

    // Add X axis label:
    this.svg.append("text")
      .attr("text-anchor", "end")
      .attr("x", this.width/2 + this.margin)
      .attr("y", this.height + 30)
      .attr("fill", "#FFFFFF")
      .text("Risk (σ)");

    // Y axis label:
    this.svg.append("text")
      .attr("text-anchor", "end")
      .attr("transform", "rotate(-90)")
      .attr("y", -this.margin + 20)
      .attr("x", -this.margin - this.height/2 + 20)
      .attr("fill", "#FFFFFF")
      .text("Expected Return")

    const color = d3.scaleOrdinal()
      .domain(["holdings", "frontier"])
      .range(["#619CFF", "#00BA38"])
    
    // Add dots
    this.svg.append('g')
      .selectAll("dot")
      .data(this.holdings)
      .enter()
      .append("circle")
        .attr("cx", function (d) { return x(d.sigma); } )
        .attr("cy", function (d) { return y(d.er); } )
        .attr("r", 5)
        .style("fill", function (d) { return color('holdings') } )
        .on("mouseover", holdingMouseover)
        .on("mousemove", holdingMousemove)
        .on("mouseleave", holdingMouseleave)
    
    // Add the lines
    this.svg.append("path")
      .datum(this.frontier.map(f => ([f.sigma, f.er])))
      .attr("fill", "none")
      .attr("stroke", "#69b3a2")
      .attr("stroke-width", 1.5)
      .attr("d", d3.line()
        .x(function(d) { return x(d[0]) })
        .y(function(d) { return y(d[1]) })
      )
  }
}
