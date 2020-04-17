import {Component, OnInit} from '@angular/core';
import {CompanyService} from "../company.service";
import {Company} from "../models";

@Component({
  selector: 'app-company-list',
  templateUrl: './company-list.component.html',
  styleUrls: ['./company-list.component.css']
})
export class CompanyListComponent implements OnInit {
  companies: Company[] = [];

  constructor(public companyService: CompanyService) {
  }

  ngOnInit(): void {
    this.getCompanyList();
  }

  getCompanyList() {
    this.companyService.getCompanyList()
      .subscribe(companies => {
        this.companies = companies
      });
  }

  deleteCompany(id) {
    this.companyService.deleteCompany(id).subscribe(res => {
      // this.categories = this.categories.filter(c => c.id != id);
      // this.getCategoryList();
    });
  }

}