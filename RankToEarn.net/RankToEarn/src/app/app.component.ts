import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute, Route, Router, RoutesRecognized, NavigationEnd } from '@angular/router';
import { Subscription } from 'rxjs';
import { SetIdService } from './service/set-id.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'RankToEarn';

  isTablePage = true;
  isProfilePage:boolean;
  id:any;
  page_id:number;
  page:any;
  subscription1:Subscription;
  subscription2:Subscription;

  constructor(
    private router:Router,
    private route:ActivatedRoute,
    public service_id:SetIdService
  ) {
   
  }


  ngOnInit(): void {
    
    this.subscription1 = this.router.events.subscribe(event => {
      if (event instanceof RoutesRecognized) {
        try{
          let route = event.state.root.firstChild;
          this.id = route!.data['id'] || '';
          this.page_id = Number(this.id); 
          this.service_id.setId(this.page_id);
          console.log('app comp* Id passed through URL:', this.id);
        }
        catch(e){}
      
      }
    });

    //Redirects Home -> ?page=1
    this.subscription2 = this.router.events.subscribe((event) => {
      if(event instanceof NavigationEnd){
        if(event.url == '/') {
          this.router.navigate([''],{
            queryParams: {'page': 1},
            queryParamsHandling: 'merge'
          });
        }
      }
      else {
        null;
      }
    });

    console.log('router = ',this.router.getCurrentNavigation());
  }

  ngOnDestroy(): void {
    console.log('app comp * ngOnDestroy Called :O');
    this.subscription1.unsubscribe();
    this.subscription2.unsubscribe();
  }


}
