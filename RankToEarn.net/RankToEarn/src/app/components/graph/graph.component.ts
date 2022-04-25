import { Component, Input, OnInit } from '@angular/core';
import Chart from 'chart.js/auto';
import datajson from './json_data_appended.json';

@Component({
  selector: 'app-graph',
  templateUrl: './graph.component.html',
  styleUrls: ['./graph.component.css']
})
export class GraphComponent implements OnInit {

  make_chart_arg(name:string, X:string[],Y:number[], color:string){
    
    var myChart_ = new Chart(name, {
      
      type: 'line',
      data: {
        labels: X,
        datasets: [{
          label: name,
          data: Y,
          backgroundColor: 
            color
          ,
          borderColor:
            color,
          borderWidth: 2.5,
          tension: 0.5,
          pointRadius: 0
          }],
      },
      options: {
          scales: {
              x: {
                ticks: {
                  display:true
                } 
              },
              y: {
                beginAtZero:false
              }
          }
      }
    });
    
    return myChart_;
    
  }

  //charty = "charty";

  @Input()
  name:string;

  chart1:Chart;
  chart2:Chart;
  chart3:Chart;

  constructor() { }

  ngOnInit(): void {

  }
  ngAfterViewInit(): void {
    var opt = 0;
    for(let i=0;i<datajson.tables.length;i++) {
      if(datajson.tables[i].name === this.name)
      opt = i;
    }
    var num = Math.floor(Math.random()*16777215).toString(16);
    var color = "#"+num.toString();
  
    this.make_chart_arg(this.name,datajson.tables[opt].dates,datajson.tables[opt].members,color);

  }

}
