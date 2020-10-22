import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { ModelPortfoliosPage } from './model-portfolios.page';

describe('PortfoliosPage', () => {
  let component: ModelPortfoliosPage;
  let fixture: ComponentFixture<ModelPortfoliosPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModelPortfoliosPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(ModelPortfoliosPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
