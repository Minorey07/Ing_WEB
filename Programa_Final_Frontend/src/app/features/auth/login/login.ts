import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../../../services/auth.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './login.html',
  styleUrl: './login.css'
})
export class Login {

  correo: string = '';
  password: string = '';
  mensaje: string = '';

  constructor(
    private authService: AuthService,
    private router: Router
  ) {}

  async ingresar(): Promise<void> {
    const ok = await this.authService.login(this.correo, this.password);
    if (!ok) {
      this.mensaje = 'Credenciales incorrectas';
      return;
    }
    this.router.navigate(['/dashboard']);
  }
}
