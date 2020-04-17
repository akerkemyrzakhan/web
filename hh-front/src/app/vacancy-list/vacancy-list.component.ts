import {Component, OnInit} from '@angular/core';
import {Vacancy} from '../vacancy';
import {CompanyService} from '../company.service';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-vacancy-list',
  templateUrl: './vacancy-list.component.html',
  styleUrls: ['./vacancy-list.component.css']
})
export class VacancyListComponent implements OnInit {
  vacancies: Vacancy[];

  constructor(private companyService: CompanyService,public route: ActivatedRoute) {}

  ngOnInit(): void {
    this.getVacanciesList();
  }

  getVacanciesList() {
    let id = this.route.snapshot.paramMap.get('id');
    id = id.substr(1);
    this.companyService.getVacancyList(id)
      .subscribe(vacancies => {
        this.vacancies = vacancies;
      });
  }

}
