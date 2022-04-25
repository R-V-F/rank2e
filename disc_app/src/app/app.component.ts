import { Component, ViewChild, OnInit, ElementRef } from '@angular/core';
import Chart from 'chart.js/auto';
import {CdkTableModule} from '@angular/cdk/table';
import {MatTableModule} from '@angular/material/table';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  toggle = 2;

  title = 'disc_app';
  display_graph = false;
  display_table = true;
  changeView(graph:boolean, table:boolean) {
    this.display_graph = graph;
    
    this.display_table = table;
    console.log(graph, table);
  }



}
