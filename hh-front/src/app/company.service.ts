import {Injectable} from '@angular/core';
import {Observable, of} from 'rxjs';
import {HttpClient} from "@angular/common/http";
import {Company, LoginResponse} from "./models";
import {Vacancy} from './vacancy';
@Injectable({
  providedIn: 'root'
})
export class CompanyService {
  BASE_URL = 'http://localhost:8000'
  constructor(private http: HttpClient) {}

  getCompanyList(): Observable<Company[]> {
    return this.http.get<Company[]>(`${this.BASE_URL}/hh/companies/`);
  }
  getVacancyList(id): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(`${this.BASE_URL}/api/companies/${id}/vacancies/`);
  }

  getCompany(id): Observable<Company> {
    return this.http.get<Company>(`${this.BASE_URL}/hh/companies/${id}/`);
  }

  deleteCompany(id): Observable<any> {
    return this.http.delete(`${this.BASE_URL}/hh/companies/${id}/`);
  }

  login(username, password): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`${this.BASE_URL}/hh/login/`, {
      username,
      password
    })
  }
}