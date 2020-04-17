import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {HttpClientModule} from '@angular/common/http';
import { CompanyListComponent } from './company-list/company-list.component';
import {HTTP_INTERCEPTORS} from '@angular/common/http';
import {FormsModule} from '@angular/forms';
import{AuthInterceptor} from './auth.interceptor';
import { CompanyPageComponent } from './company-page/company-page.component';
import { VacancyListComponent } from './vacancy-list/vacancy-list.component';
@NgModule({
  declarations: [
    AppComponent,
    CompanyListComponent,
    CompanyPageComponent,
    VacancyListComponent
  
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
  ],
  providers: [
    {
      provide:HTTP_INTERCEPTORS,
      useClass:AuthInterceptor,
      multi:true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
