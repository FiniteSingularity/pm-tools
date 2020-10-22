import { Component, OnInit } from '@angular/core';
import { ModelPortfolio } from '@app/models/portfolio.models';
import { NavController } from '@ionic/angular';
import { ModelPortfolioService } from '@services/api/model-portfolio.service';

@Component({
  selector: 'app-model-portfolios',
  templateUrl: './model-portfolios.page.html',
  styleUrls: ['./model-portfolios.page.scss'],
})
export class ModelPortfoliosPage implements OnInit {
  modelPortfolios: ModelPortfolio[] = [];

  constructor(
    private modelPortSrvc: ModelPortfolioService,
    private navCtrl: NavController
  ) { }

  ngOnInit() {
    this.getModelPortData();
  }

  async getModelPortData() {
    this.modelPortSrvc.loadAll().subscribe((res) => {
      this.modelPortfolios = res.results;
      console.log(res.results);
    })
  }

  portfolioClicked(port: ModelPortfolio) {
    const id = port.id;
    this.navCtrl.navigateForward(['/private', 'model-portfolios', `${id}`]);
  }
}
