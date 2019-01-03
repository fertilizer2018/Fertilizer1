import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ShoperHomeComponent } from './shoper-home.component';

describe('ShoperHomeComponent', () => {
  let component: ShoperHomeComponent;
  let fixture: ComponentFixture<ShoperHomeComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ShoperHomeComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ShoperHomeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
