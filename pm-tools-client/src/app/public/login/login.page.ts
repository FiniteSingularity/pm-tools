import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from '@services/auth/authentication.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage implements OnInit {
  username: string;
  password: string;

  constructor(private auth: AuthenticationService) { }

  ngOnInit() {
  }

  login() {
    this.auth.login({ 
      username: this.username,
      password: this.password
    });
  }
}
