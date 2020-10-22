import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ModelPortfolio, ModelPortHoldingBeta } from '@app/models/portfolio.models';
import { ModelPortfolioService } from '@services/api/model-portfolio.service';

@Component({
  selector: 'app-model-portfolio',
  templateUrl: './model-portfolio.page.html',
  styleUrls: ['./model-portfolio.page.scss'],
})
export class ModelPortfolioPage implements OnInit {
  portfolioId: string;
  modelPortfolio: ModelPortfolio;
  holdingBetas: ModelPortHoldingBeta[] = [];
  constructor(private modelPortSvc: ModelPortfolioService, private route: ActivatedRoute) { }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.portfolioId = params.get('id');
      this.modelPortSvc.load(this.portfolioId).subscribe( res => {
        this.modelPortfolio = res;
        console.log(res);
      });
      this.modelPortSvc.holdingBetas(this.portfolioId).subscribe( res => {
        this.holdingBetas = res.betas;
      })
    });
  }

}
