import { Component, OnInit, Output, EventEmitter, Input, AfterViewInit, OnChanges, SimpleChanges, OnDestroy } from '@angular/core';

import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit, OnDestroy {
  
  @Output() getPage:EventEmitter<any> = new EventEmitter;
  @Input() num_pages:number;
  @Input() current_page:number;

  subscription: Subscription;
  page_actv:number;

  constructor(private route:ActivatedRoute) {

  }

  ngOnInit(): void {
    this.subscription = this.route.queryParams.subscribe
    ((queryParams:any) => {
      try{
        this.page_actv = queryParams['page'];
        if(this.page_actv){
          //Set the current page button to disabled and scroll to the start of the table
          for(let i = 0; i < this.num_pages; i++){
            let element_off = "but"+String(i+1);
            
            document.getElementById(element_off)!.removeAttribute("disabled");
          }
          let element = "but"+String(this.page_actv);
          
          document.getElementById(element)!.setAttribute("disabled","disabled");
          window.scrollTo(0, 0);
          
        }
      }
      catch(e) {
        console.log(e);
      }
    });

  }


  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }

  emitPage($event:number) {
    this.getPage.emit($event);
  }

  isCurrent(current_page:number){
    if(this.page_actv == current_page) {
      return true;
    }
    else return false;
  }

}
