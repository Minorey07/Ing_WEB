import { CanActivateFn, Router } from '@angular/router';
import { inject } from '@angular/core';
import { AuthService } from '../services/auth.service';

export const roleGuard = (rolesPermitidos: string[]): CanActivateFn => {

  return () => {

    const authService = inject(AuthService);
    const router = inject(Router);

    const rol = authService.getRol();

    if (rol && rolesPermitidos.includes(rol)) {
      return true;
    }

    router.navigate(['/dashboard']);
    return false;
  };
};