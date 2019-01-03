import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { HttpClientModule } from "@angular/common/http";
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MaterialModule } from './material.module';
import { RegisterCompComponent } from './register-comp/register-comp.component';
import { from } from 'rxjs';

//auth component
import { SignupComponent } from './auth/signup/signup.component';
import { LoginComponent } from './auth/login/login.component';

//farmer component
import { FarmerHomeComponent } from './farmer/farmer-home/farmer-home.component';

//shoper component
import { ShoperHomeComponent } from './shoper/shoper-home/shoper-home.component';

@NgModule({
  declarations: [
    AppComponent,
    RegisterCompComponent,
    SignupComponent,
    LoginComponent,
    FarmerHomeComponent,
    ShoperHomeComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MaterialModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
