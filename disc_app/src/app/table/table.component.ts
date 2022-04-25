import { Component, OnInit } from '@angular/core';
import {CdkTableModule} from '@angular/cdk/table';
import {MatTableModule} from '@angular/material/table';
import datajson from './json_data_modified.json';
import {MatSort, Sort} from '@angular/material/sort';
import {MatTableDataSource} from '@angular/material/table';
import {LiveAnnouncer} from '@angular/cdk/a11y';
import {AfterViewInit, ViewChild} from '@angular/core';
import { NgModule } from '@angular/core';
import {FormsModule} from '@angular/forms';
import { MatPaginator } from '@angular/material/paginator';
import { MatFormField } from '@angular/material/form-field';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})


export class TableComponent implements OnInit, AfterViewInit {
  displayedColumns: string[] = ['name', 'size','weekly'];
  dataSource2:any = [];
  name_test:string = datajson.tables[5].name;
  i=0;
  n_tables = datajson.tables.length;
  namej:string;
  opened = false;



  constructor(private _liveAnnouncer: LiveAnnouncer) {
    for (let i=0 ; i < this.n_tables ;i++) {
      var source_obj = {name:"aa", size:3, weekly:1.1};

      source_obj.name = datajson.tables[i].name;
      //pick last data available
      source_obj.size = datajson.tables[i].members[(datajson.tables[i].members.length)-1];
      if(datajson.tables[i].members[(datajson.tables[i].members.length)-1] != 0 && datajson.tables[i].members[(datajson.tables[i].members.length)-8] != 0) {
        var ratio = (datajson.tables[i].members[(datajson.tables[i].members.length)-1]) / (datajson.tables[i].members[(datajson.tables[i].members.length)-8]);
        ratio = (ratio-1)*100;
        ratio = Math.round(ratio * 100) / 100;
        source_obj.weekly = ratio;
        console.log(source_obj.weekly);
      }
      else {
        source_obj.weekly = -99.0;
      }




      this.dataSource2.push(source_obj);

    }
   }

  dataSource = new MatTableDataSource(this.dataSource2)

  @ViewChild(MatSort) sort: MatSort;
  @ViewChild(MatPaginator) paginator:MatPaginator;

  ngOnInit(): void {
    
  }

  ngAfterViewInit() {

    this.dataSource.sort = this.sort;
    this.dataSource.paginator = this.paginator;
  }

  applyFilter(event:Event){
    var filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

  }

}
