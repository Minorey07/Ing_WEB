import { Injectable } from '@angular/core';
import { BaseHttpService } from './base-http.service';
import { Proveedor } from '../models/proveedor.model';

@Injectable({ providedIn: 'root' })
export class ProveedorService {
  constructor(private http: BaseHttpService) {}

  listar(): Promise<Proveedor[]> {
    return this.http.get<Proveedor[]>('/proveedores/');
  }

  crear(proveedor: Proveedor): Promise<Proveedor> {
    return this.http.post<Proveedor>('/proveedores/', proveedor);
  }

  actualizar(proveedor: Proveedor): Promise<Proveedor> {
    return this.http.put<Proveedor>(`/proveedores/${proveedor.id}`, proveedor);
  }

  eliminar(id: number): Promise<void> {
    return this.http.delete<void>(`/proveedores/${id}`);
  }
}
