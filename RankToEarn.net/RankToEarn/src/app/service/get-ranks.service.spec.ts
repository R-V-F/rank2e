import { TestBed } from '@angular/core/testing';

import { GetRanksService } from './get-ranks.service';

describe('GetRanksService', () => {
  let service: GetRanksService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GetRanksService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
