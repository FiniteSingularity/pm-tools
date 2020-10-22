import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { PortfoliosPage } from './portfolios.page';

describe('PortfoliosPage', () => {
  let component: PortfoliosPage;
  let fixture: ComponentFixture<PortfoliosPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PortfoliosPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(PortfoliosPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
