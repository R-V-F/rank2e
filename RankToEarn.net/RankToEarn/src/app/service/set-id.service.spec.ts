import { TestBed } from '@angular/core/testing';

import { SetIdService } from './set-id.service';

describe('SetIdService', () => {
  let service: SetIdService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SetIdService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
