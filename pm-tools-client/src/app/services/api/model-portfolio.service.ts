import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ModelPortfolio, ModelPortfolioListResponse, ModelPortHoldingsBetaResponse } from '@app/models/portfolio.models';
import { Observable } from 'rxjs';
import { ApiService } from './api.service';

@Injectable({
  providedIn: 'root'
})
export class ModelPortfolioService {

  constructor(private http: HttpClient, private api: ApiService) {}

  loadAll(page: number = 1): Observable<ModelPortfolioListResponse> {
    return this.http.get<ModelPortfolioListResponse>(
      `${this.api.url}/model-portfolios`
    );
  }

  load(id: string): Observable<ModelPortfolio> {
    return this.http.get<ModelPortfolio>(
      `${this.api.url}/model-portfolios/${id}`
    );
  }

  holdingBetas(id: string): Observable<ModelPortHoldingsBetaResponse> {
    return this.http.get<ModelPortHoldingsBetaResponse>(
      `${this.api.url}/model-portfolios/${id}/holding-betas`
    );
  }
}
