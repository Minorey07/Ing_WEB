import { Component, inject, signal } from '@angular/core';
import { DatePipe } from '@angular/common';
import { Compra } from '../../models/compra.model';
import { Proveedor } from '../../models/proveedor.model';
import { CompraService } from '../../services/compra.service';
import { ProveedorService } from '../../services/proveedor.service';

@Component({
  selector: 'app-compra-component',
  imports: [DatePipe],
  templateUrl: './compra-component.html',
  styleUrl: './compra-component.css',
})
export class CompraComponent {
  compraService = inject(CompraService);
  proveedorService = inject(ProveedorService);
  listaCompras = signal<Compra[]>([]);
  listaProveedores = signal<Proveedor[]>([]);
  modoEdicion = false;
  idEditando = 0;

  constructor() {
    this.cargarCompras();
    this.cargarProveedores();
  }

  async cargarCompras() {
    const data = await this.compraService.listar();
    console.log("COMPRAS RESPONSE:", data);
    this.listaCompras.set(data);
  }

  async cargarProveedores() {
    this.listaProveedores.set(await this.proveedorService.listar());
  }

  modeloCompra = signal<Compra>({ id: 0, proveedorId: 0, total: 0 });

  getNombreProveedor(id: number): string {
    const p = this.listaProveedores().find(pv => pv.id === id);
    return p ? p.razonSocial : 'Sin proveedor';
  }

  seleccionarProveedor(event: Event) {
    const value = Number((event.target as HTMLSelectElement).value);
    this.modeloCompra.set({ ...this.modeloCompra(), proveedorId: value });
  }

  actualizarTotal(event: Event) {
    const value = Number((event.target as HTMLInputElement).value);
    this.modeloCompra.set({ ...this.modeloCompra(), total: value });
  }

  async guardar(event: Event) {
    event.preventDefault();
    let compra: Compra = {
      id: this.idEditando,
      proveedorId: this.modeloCompra().proveedorId,
      total: this.modeloCompra().total,
    };
    if (this.modoEdicion) {
      await this.compraService.actualizar(compra);
      this.modoEdicion = false;
      this.idEditando = 0;
    } else {
      await this.compraService.crear(compra);
    }
    await this.cargarCompras();
    this.limpiarFormulario();
  }

  editar(compra: Compra) {
    this.modoEdicion = true;
    this.idEditando = compra.id;
    this.modeloCompra.set({ ...this.modeloCompra(), proveedorId: compra.proveedorId, total: compra.total });
  }

  async eliminar(id: number) {
    await this.compraService.eliminar(id);
    await this.cargarCompras();
  }

  limpiarFormulario() {
    this.modeloCompra.set({ id: 0, proveedorId: 0, total: 0 });
  }

  get totalCompras(): number {
    return this.listaCompras().reduce((t, c) => t + c.total, 0);
  }
}
