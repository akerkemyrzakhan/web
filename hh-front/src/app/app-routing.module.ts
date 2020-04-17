import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CompanyListComponent } from './company-list/company-list.component';
import { CompanyPageComponent } from './company-page/company-page.component';
import {VacancyListComponent} from './vacancy-list/vacancy-list.component';

const routes: Routes = [
  { path: '', component: CompanyListComponent },
  { path: 'category/:id', component: CompanyPageComponent },
  {path: 'company/:id/vacancies', component: VacancyListComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }