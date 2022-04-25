import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TableComponent } from './components/table/table.component';
import {MatSort, MatSortModule, Sort} from '@angular/material/sort';
import { MatPaginatorModule } from '@angular/material/paginator';
import {MatFormFieldModule} from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatTableModule} from '@angular/material/table';
import {MatButtonToggleModule} from '@angular/material/button-toggle';




import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';


import { FormsModule } from '@angular/forms';
import { GraphComponent } from './components/graph/graph.component';
import { FooterComponent } from './components/footer/footer.component';
import { HeaderComponent } from './components/header/header.component';
import { NavbarComponent } from './components/table/navbar/navbar.component';
import { PageComponent } from './components/page/page.component';

@NgModule({
  declarations: [
    AppComponent,
    TableComponent,
    GraphComponent,
    FooterComponent,
    HeaderComponent,
    NavbarComponent,
    PageComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatIconModule,
    MatSortModule,
    MatPaginatorModule,
    MatFormFieldModule,
    MatInputModule,
    BrowserAnimationsModule,
    MatTableModule,
    FormsModule,
    MatButtonModule,
    MatButtonToggleModule
    


  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
