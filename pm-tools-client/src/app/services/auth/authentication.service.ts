import { catchError } from 'rxjs/operators';
import { ApiService } from '../api/api.service';
import { NavController, Platform } from '@ionic/angular';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Subscription, throwError } from 'rxjs';
import { Storage } from '@ionic/storage';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

const TOKEN_KEY = 'authToken';
const BASE_URL_KEY = 'baseApiUrl';
const BASE_URL = environment.apiUrl;

export interface ApiAuth {
  token: string;
}

export interface AuthStatus extends ApiAuth {
  authenticated: boolean;
  loginError: string;
}

@Injectable({
  providedIn: 'root',
})
export class AuthenticationService {
  authenticationState = new BehaviorSubject<AuthStatus>({
    authenticated: false,
    token: '',
    loginError: null,
  });

  loginSub: Subscription;
  firstLoginSub: Subscription;
  token = '';
  private readyPromise: Promise<string>;

  constructor(
    private storage: Storage,
    private plt: Platform,
    private http: HttpClient,
    private api: ApiService,
    private navCtrl: NavController,
  ) {
    let readyResolve: (value: string) => void;
    this.readyPromise = new Promise((res) => {
      readyResolve = res;
    });

    this.plt.ready().then(() => {
      this.checkStorage().then(() => {
        readyResolve('ready');
      });
    });
  }

  async ready() {
    return this.readyPromise;
  }

  login(payload: { username: string; password: string }) {
    this.loginSub = this.http
      .post<ApiAuth>(`${BASE_URL}/api-token-auth/`, payload)
      .subscribe(
        async (data) => {
          const promises = [this.storage.set(TOKEN_KEY, data.token)];
          const res = await Promise.all(promises);
          this.api.url = `${BASE_URL}`;
          this.token = data.token;
          this.authenticationState.next({
            authenticated: true,
            loginError: null,
            ...data,
          });
          this.navCtrl.navigateRoot(['/']);
        },
        (error) => {
          console.log('error!');
          this.api.url = '';
          this.authenticationState.next({
            authenticated: false,
            token: '',
            loginError: 'Incorrect Username or Password',
          });
          return null;
        }
      );
  }

  async logout() {
    const promises = [
      this.storage.remove(TOKEN_KEY),
      this.storage.remove(BASE_URL_KEY),
    ];
    const data = await Promise.all(promises);
    this.api.url = '';
    this.authenticationState.next({
      authenticated: false,
      token: '',
      loginError: 'You have been logged out.',
    });
  }

  async authenticationStatus() {
    await this.ready();
    return this.authenticationState.value;
  }

  async checkStorage() {
    const keys = [
      TOKEN_KEY,
      BASE_URL_KEY,
    ];
    const res = await this.getMultipleKeys(keys);
    if (res) {
      const auth = TOKEN_KEY in res && res[TOKEN_KEY] ? true : false;
      console.log(`setting api url to ${res[BASE_URL_KEY]}`);
      this.api.url = `${BASE_URL}`;
      this.token = res[TOKEN_KEY];
      const state: AuthStatus = {
        authenticated: auth,
        token: res[TOKEN_KEY],
        loginError: '',
      };
      this.authenticationState.next(state);
    } else {
      this.api.url = '';
      this.token = '';
      const state: AuthStatus = {
        authenticated: false,
        token: '',
        loginError: null,
      };
      this.authenticationState.next(state);
    }
  }

  async getMultipleKeys(keys: string[]) {
    const promises = [];

    keys.forEach((key) => promises.push(this.storage.get(key)));

    const values = await Promise.all(promises);
    const result = {};
    values.map((value, index) => {
      result[keys[index]] = value;
    });
    return result;
  }
}
