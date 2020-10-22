import { PaginatedResponse } from './api.models';

export interface ModelPortfolio {
    id: number;
    name: string;
}

export interface ModelPortfolioListResponse extends PaginatedResponse {
    results: ModelPortfolio[];
}

export interface ModelPortHoldingBeta {
    ticker: string;
    beta: number;
}

export interface ModelPortHoldingsBetaResponse {
    betas: ModelPortHoldingBeta[];
}