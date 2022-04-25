import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SetIdService {
  private page_id = new BehaviorSubject(0);
  constructor() { }

  setId(id: number): void {
    this.page_id.next(id);
  }

  getUser(): Observable<number> {
    return this.page_id.asObservable();
  }

  
}
