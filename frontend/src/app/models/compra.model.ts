import { CompraDetalle } from './compra-detalle.model';

export interface Compra {
  id: number;
  proveedorId: number;
  proveedorNombre?: string;
  createdAt?: string;
  total: number;
  detalles?: CompraDetalle[];
  expandida?: boolean;
}