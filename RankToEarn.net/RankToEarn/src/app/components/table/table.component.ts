import { Component, OnChanges, OnDestroy, OnInit, SimpleChanges } from '@angular/core';

import datajson from './json_data_appended_and_sorted.json';

import {MatTableDataSource} from '@angular/material/table';
import {LiveAnnouncer} from '@angular/cdk/a11y';
import {AfterViewInit, ViewChild} from '@angular/core';

import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';


@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent implements OnInit, OnDestroy {
  

  displayedColumns: string[] = ['rank','thumbnail','name', 'size','weekly','monthly', 'followers','f_weekly', 'f_monthly','socials'];
  dataSource2:any = [];
  
  i=0;
  n_tables = datajson.tables.length;
  namej:string;
  opened = false;
  help:number;
  helpI:number;
  dataSource_page:any = [];
  page_tables:any = []; // ** [[50 items],[50 items],[50 items],[50 items]...]
  page: number;
  num_pages = 17; /** To Do: calculate this dinamically */
  sortBy: any;
  subscription1: Subscription;
  subscription2: Subscription;
  subscription3: Subscription;
  socials:any = datajson.tables[0].socials;




  /** Variables to handle sorting.
   *  It's whacky, change this later.
   */

  sort_states = ['none','asc','dsc'];
  sort_state_weekly = 0;
  sort_state_monthly = 0;
  sort_state_followers = 0;
  sort_state_size = 0;
  sort_state_f_weekly = 0;
  sort_state_f_monthly = 0;
  

  constructor(
        private _liveAnnouncer: LiveAnnouncer,
        private route:ActivatedRoute,
        private router:Router
  ){
    /**
     *  Since dumping everything at once on the table was taking a huge toll on the site performance,
     *  the table is loading only what's been displeyed.
     *  The following steps separetes the json_data content into 'buckets' of 50 items. Then, when the user
     *  changes page, the page var is updated and the correct 'bucket' is loaded. 
     */

    
    for (let i=0 ; i < this.n_tables ;i++) {
      var source_obj = {id:0, name:"aa", socials:{twitter:"none",discord:"none",home_page:"none"}, size:3, weekly:1.1, monthly:3, followers: 2, f_weekly: 1, f_monthly: 2, img_path:"bb", route: "rout"};
      //PROJECT ID SET
      source_obj.id = datajson.tables[i].id;
      // PROJECT NAME SET
      source_obj.name = datajson.tables[i].name;
      // PROJECT ROUTE SET
      source_obj.route = datajson.tables[i].route;
      // PROJECT SOCIALS SET
      source_obj.socials.twitter = datajson.tables[i].socials.twitter;
      source_obj.socials.discord = datajson.tables[i].socials.discord;
      source_obj.socials.home_page = datajson.tables[i].socials.home_page;

      // DISCORD SIZE SET
      if(datajson.tables[i].members[(datajson.tables[i].members.length)-1] > 0) {
        source_obj.size = datajson.tables[i].members[(datajson.tables[i].members.length)-1];
      }
      else {
        source_obj.size = -99
      }

      // TWITTER FOLLOWERS SET
      if(datajson.tables[i].followers[(datajson.tables[i].followers.length)-1] > 0){
        source_obj.followers = datajson.tables[i].followers[(datajson.tables[i].followers.length)-1];
      }
      else {
        source_obj.followers = -99
      }


      // DISCORD WEEKLY SET
      if(datajson.tables[i].members[(datajson.tables[i].members.length)-1] != 0 && datajson.tables[i].members[(datajson.tables[i].members.length)-8] != 0 && datajson.tables[i].members.length > 6) {
        var ratio = (datajson.tables[i].members[(datajson.tables[i].members.length)-1]) / (datajson.tables[i].members[(datajson.tables[i].members.length)-8]);
        ratio = (ratio-1)*100;
        ratio = Math.round(ratio * 100) / 100;
        source_obj.weekly = ratio;
      }
      else {
        source_obj.weekly = -99;
      }

      //DISCORD MONTHLY SET
      if(datajson.tables[i].members[(datajson.tables[i].members.length)-1] != 0 && datajson.tables[i].members[(datajson.tables[i].members.length)-31] != 0 && datajson.tables[i].members.length > 29) {
        var ratio = (datajson.tables[i].members[(datajson.tables[i].members.length)-1]) / (datajson.tables[i].members[(datajson.tables[i].members.length)-31]);
        ratio = (ratio-1)*100;
        ratio = Math.round(ratio * 100) / 100;
        source_obj.monthly = ratio;
      }
      else {
        source_obj.monthly = -99;
      }

      // TWITTER WEEKLY SET
      if(datajson.tables[i].followers[(datajson.tables[i].followers.length)-1] != 0 && datajson.tables[i].followers[(datajson.tables[i].followers.length)-8] != 0 && datajson.tables[i].followers.length > 6) {
        var ratio = (datajson.tables[i].followers[(datajson.tables[i].followers.length)-1]) / (datajson.tables[i].followers[(datajson.tables[i].followers.length)-8]);
        ratio = (ratio-1)*100;
        ratio = Math.round(ratio * 100) / 100;
        source_obj.f_weekly = ratio;
      }
      else {
        source_obj.f_weekly = -99;
      }

      // TWITTER MONTHLY SET
      if(datajson.tables[i].followers[(datajson.tables[i].followers.length)-1] != 0 && datajson.tables[i].followers[(datajson.tables[i].followers.length)-31] != 0 && datajson.tables[i].followers.length > 29) {
        var ratio = (datajson.tables[i].followers[(datajson.tables[i].followers.length)-1]) / (datajson.tables[i].followers[(datajson.tables[i].followers.length)-31]);
        ratio = (ratio-1)*100;
        ratio = Math.round(ratio * 100) / 100;
        source_obj.f_monthly = ratio;
      }
      else {
        source_obj.f_monthly = -99;
      }

      source_obj.img_path = datajson.tables[i].img_path;
      




      this.dataSource2.push(source_obj);

    }
    

    let i=1,j=0;
    for(i;i < this.dataSource2.length; i++) {
      for (j = 0; j < this.dataSource2.length - i; j++){
        if(this.dataSource2[j].size < this.dataSource2[j+1].size) {
          let aux = this.dataSource2[j];

          this.dataSource2[j] = this.dataSource2[j+1];
          
          this.dataSource2[j+1] = aux;

        }
      }
      
    } //sorted dataSource2 by dicord size

    /** Push only 50 items to the front page table.
     *  This is done so the table don't load everything at once,
     *  avoinding the toll on performance.
     */
    for (let i=0 ; i < 50 ;i++) {
      this.dataSource_page.push(this.dataSource2[i]);
    }

    /** Create a list of lists(size 50):
     *    The index of the inner list represents the content of the table in a given page.
     *    Ex: page_tables[2] <- table content of page 3 
     */

    let single_page = [];

    for (let i = 0; i < this.n_tables; i++) {
      
      single_page.push(this.dataSource2[i]);
      if ((i+1) % 50 == 0) {
        this.page_tables.push(single_page);
        
        single_page = [];
      }
      if(i == this.n_tables-1) {
        this.page_tables.push(single_page);
      }
    }






  }

  sortData(sort_by:string, sort_direction:string) {
    
    

    if(sort_by == 'size' || sort_by == 'weekly' || sort_by == 'monthly' || sort_by == 'followers' || sort_by == 'f_weekly' || sort_by == 'f_monthly') {      

      if(sort_direction == 'asc') {
        this.page_tables.length = 0 /*method sugested to empty array */
        let i=1,j=0;
        for(i;i < this.dataSource2.length; i++) {
          for (j = 0; j < this.dataSource2.length - i; j++){
            if(this.dataSource2[j][sort_by] > this.dataSource2[j+1][sort_by]) {
              let aux = this.dataSource2[j];

              this.dataSource2[j] = this.dataSource2[j+1];
              
              this.dataSource2[j+1] = aux;

            }
          }
          
        } //sorted dataSource2 by weekly asc
        let single_page = [];

        for (let i = 0; i < this.n_tables; i++) {
          
          single_page.push(this.dataSource2[i]);
          if ((i+1) % 50 == 0) {
            this.page_tables.push(single_page);
            
            single_page = [];
          }
          if(i == this.n_tables-1) {
            this.page_tables.push(single_page);
          }
        } // making the buckets

      }

      else if(sort_direction == 'dsc') {
        this.page_tables.length = 0 /*method sugested to empty array */
        let i=1,j=0;
        for(i;i < this.dataSource2.length; i++) {
          for (j = 0; j < this.dataSource2.length - i; j++){
            if(this.dataSource2[j][sort_by] < this.dataSource2[j+1][sort_by]) {
              let aux = this.dataSource2[j];

              this.dataSource2[j] = this.dataSource2[j+1];
              
              this.dataSource2[j+1] = aux;

            }
          }
          
        } //sorted dataSource2 by weekly dsc
        let single_page = [];

        for (let i = 0; i < this.n_tables; i++) {
          
          single_page.push(this.dataSource2[i]);
          if ((i+1) % 50 == 0) {
            this.page_tables.push(single_page);
            
            single_page = [];
          }
          if(i == this.n_tables-1) {
            this.page_tables.push(single_page);
          }
        } // making the buckets

      }
      else {
        console.log('cool bro:', sort_direction);
      }

    }

    else {
      console.log('smth went veri veri wrong with sortby');
    }

    



  }


  dataSource = new MatTableDataSource(this.dataSource_page);

  

  ngOnInit(): void {
    

    this.subscription1 = this.route.queryParams.subscribe
    ((queryParams:any) => {
      this.page = queryParams['page'];
      console.log('Table-Comp* ngOnInit this.page =', this.page);
    });


    this.subscription2 = this.route.queryParams.subscribe
    ((queryParams:any) => {
      this.sortBy = queryParams['sortBy'];
      if(this.sortBy) {
        console.log('Table-Comp* ngOnInit this.sortBy =', this.sortBy);
      }

    });


    this.subscription3 = this.route.queryParams.subscribe
    ((queryParams:any) => {
      let dir = queryParams['direction'];

      if(this.sortBy) {
        console.log('Table-Comp* ngOnInit direction =', dir);
      }

      if(this.page && this.sortBy){
        console.log('table-Comp* calling sortData and getPage. this.sortBy = ', this.sortBy);
        this.sortData(this.sortBy, dir);
        this.getPage(this.page);
      }
  

    });

    console.log('table comp * first call of ngOninit. this.page = ', this.page);

  }

  ngOnDestroy(): void {
    this.subscription1.unsubscribe();
    this.subscription2.unsubscribe();
    this.subscription3.unsubscribe();
  }

  applyFilter(event:Event){
    var filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

  }

  getPage(page:any){
    this.router.navigate([''],{
      queryParams: {'page': page},
      queryParamsHandling: 'merge'
      //queryParamsHandling: 'preserve'
    
    });

    this.dataSource = new MatTableDataSource(this.page_tables[page-1]);
  }
  sortBySize(sort:any) {
    this.sort_state_size++;
    this.sort_state_weekly = 0;
    this.sort_state_monthly = 0;
    this.sort_state_followers = 0;
    this.sort_state_f_weekly = 0;
    this.sort_state_f_monthly = 0;

    this.router.navigate([''],{
      queryParams: {sortBy: sort, direction: this.sort_states[this.sort_state_size % 3]},
      queryParamsHandling: 'merge'
    
    });
    
    console.log('Sorting Size Disc');


  }



  sortByWeekly(sort:any){
    this.sort_state_weekly++;
    this.sort_state_monthly = 0;
    this.sort_state_followers = 0;
    this.sort_state_f_weekly = 0;
    this.sort_state_f_monthly = 0;
    this.sort_state_size = 0;


    this.router.navigate([''],{
      queryParams: {sortBy: sort, direction: this.sort_states[this.sort_state_weekly % 3]},
      queryParamsHandling: 'merge'
    
    });
    
    console.log('Sorting Weekly');
  }

  sortByMonthly(sort:any){
    this.sort_state_monthly++;
    this.sort_state_followers = 0;
    this.sort_state_f_weekly = 0;
    this.sort_state_f_monthly = 0;
    this.sort_state_size = 0;
    this.sort_state_weekly = 0;

    this.router.navigate([''],{
      queryParams: {sortBy: sort, direction: this.sort_states[this.sort_state_monthly % 3]},
      queryParamsHandling: 'merge'
    
    });
    
    console.log('Sorting Weekly');



  }

  sortByFollowers(sort:any) {
    this.sort_state_followers++;
    this.sort_state_f_weekly = 0;
    this.sort_state_f_monthly = 0;
    this.sort_state_monthly = 0;
    this.sort_state_size = 0;
    this.sort_state_weekly = 0;

    this.router.navigate([''],{
      queryParams: {sortBy: sort, direction: this.sort_states[this.sort_state_followers % 3]},
      queryParamsHandling: 'merge'
    
    });
    
    console.log('Sorting Followers');

  }

  sortBy_F_Weekly(sort:any) {
    this.sort_state_f_weekly++;
    this.sort_state_f_monthly = 0;
    this.sort_state_monthly = 0;
    this.sort_state_followers = 0;
    this.sort_state_size = 0;
    this.sort_state_weekly = 0;

    this.router.navigate([''],{
      queryParams: {sortBy: sort, direction: this.sort_states[this.sort_state_f_weekly % 3]},
      queryParamsHandling: 'merge'
    
    });
    
    console.log('Sorting Followers Weekly');


  }

  sortBy_F_Monthly(sort:any) {
    this.sort_state_f_monthly++;
    this.sort_state_weekly = 0;
    this.sort_state_followers = 0;
    this.sort_state_size = 0;
    this.sort_state_monthly = 0;
    this.sort_state_f_weekly = 0;
    



    this.router.navigate([''],{
      queryParams: {sortBy: sort, direction: this.sort_states[this.sort_state_f_monthly % 3]},
      queryParamsHandling: 'merge'
    
    });
    
    console.log('Sorting Followers Weekly');

  }

  goToProfilePage(route:string) {
    console.log('goToProfilePage:', route);

    this.router.navigate([route]);
    window.scrollTo(0, 190);
  }



  


}
