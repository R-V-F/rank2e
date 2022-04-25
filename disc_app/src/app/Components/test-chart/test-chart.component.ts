import { Component, OnInit } from '@angular/core';
import Chart from 'chart.js/auto';
import { elementAt } from 'rxjs';
import data from './dbtest.json';
import datajson from './json_data_modified.json';

@Component({
  selector: 'app-test-chart',
  templateUrl: './test-chart.component.html',
  styleUrls: ['./test-chart.component.css']
})
export class TestChartComponent implements OnInit {

  option = 0;

  list_names:string[] = [];
  list_of_ids:number[] = [];

  data_add = {
    label: '# of MEMBAS',
    data: datajson.tables[5].members,
    backgroundColor: 
      'rgba(0, 99, 132, 0.2)',
    borderColor:
      'rgba(0, 99, 132, 1)',
    borderWidth: 2.5
  }

  myChart_:any;

  constructor() {
   }


  make_chart_arg(X:string[],Y:number[]){
    
    var myChart_ = new Chart("myChart", {
      
      type: 'line',
      data: {
        labels: X,
        datasets: [{
          label: '',
          data: Y,
          backgroundColor: 
            'rgba(255, 99, 132, 0.2)'
          ,
          borderColor:
            'rgba(255, 99, 132, 1)',
          borderWidth: 2.5
          }],
      },
      options: {
          scales: {
              y: {
                  beginAtZero:false
              }
          }
      }
    });

    return myChart_;
    
  }

  ngOnInit(): void {
    for(var i=0;i<datajson.tables.length;i++){
      this.list_names[i] = datajson.tables[i].name;
      this.list_of_ids[i] = i;
    }
    this.myChart_ = this.make_chart_arg([],[]);
  }

  update_chart_arg(chart:Chart, X:string[],Y:number[], color:string, label:string) {


    ///THIS ONLY WORKS BECAUSE IT'S THE FIRST ENTRYYYYY *************************************
    X.forEach((labele) => {
      chart.data.labels?.push(labele);
      console.log(chart.data.labels);
    });
    Y.forEach((numerele) => {
      chart.data.datasets.forEach((dataset) => {
        dataset.data.push(numerele);
      })
    });
    chart.data.datasets.forEach((dataset) => {
      dataset.borderColor = color;
      dataset.borderWidth = 2.5;
      dataset.backgroundColor = color;
      dataset.label = label;
    });

    chart.update();



  }

  count = 0;

  onChange(event:any){
    this.count += 1; 
    console.log(this.count);
    var num = Math.floor(Math.random()*16777215).toString(16);
    var color = "#"+num.toString();

    if(this.count == 1) {
      
      this.option = event.target.value;
      console.log('before');
      
      this.update_chart_arg(this.myChart_,datajson.tables[this.option-1].dates,datajson.tables[this.option-1].members, color,datajson.tables[this.option-1].name );
      console.log('after');

    }
    else {
      
      this.option = event.target.value;

      if(this.option!=0) { ///ignore 'SELECT' option

      
        var empt_obj:any = {};

        empt_obj.label = datajson.tables[this.option-1].name;
        empt_obj.data = datajson.tables[this.option-1].members;
        empt_obj.backgroundColor = color;
        empt_obj.borderColor = color;
        empt_obj.borderWidth = 2.5;

        this.myChart_.data.datasets.push(empt_obj);
        ///this.myChart_.data.datasets.push(empt_obj);

        

        this.myChart_.update();
      }

    }  
  }

}
