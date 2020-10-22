import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { FrontierPlotComponent } from './frontier-plot.component';

describe('FrontierPlotComponent', () => {
  let component: FrontierPlotComponent;
  let fixture: ComponentFixture<FrontierPlotComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FrontierPlotComponent ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(FrontierPlotComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
