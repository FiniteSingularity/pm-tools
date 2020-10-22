import { TestBed } from '@angular/core/testing';

import { ModelPortfolioService } from './model-portfolio.service';

describe('ModelPortfolioService', () => {
  let service: ModelPortfolioService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ModelPortfolioService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
