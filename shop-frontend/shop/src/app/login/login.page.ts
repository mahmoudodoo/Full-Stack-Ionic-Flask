import { Component, NgZone, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { DataService } from '../data.service';
import { UserService } from '../user.service';


@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage implements OnInit {
  loginFormGroup:FormGroup;
  typeError: boolean = false; 
  constructor(
    formBuilder:FormBuilder,
    private userService : UserService,
    private dataService: DataService,
    private router: Router,
    private zone: NgZone,
 

  ) { 

    this.loginFormGroup =formBuilder.group({
      username:["",[Validators.required]],
      password:["",[Validators.required]]
    });
 

  }


  onSubmit() {
    if (!this.loginFormGroup.valid) {
      return false;
    } else {
      this.userService.loginUser(this.loginFormGroup.value)
        .subscribe((response) => {
          this.zone.run(() => {
            this.loginFormGroup.reset();
            try {
            if(response['token']){
              //console.log(response)
              this.dataService.addToken('token',response['token']);
              this.router.navigate(['/home']);
            }}
            catch(TypeError){
              this.typeError = true;
              console.log(response)
            }  
          })
        });
    }
  }
 

  ngOnInit() {
  }

}
