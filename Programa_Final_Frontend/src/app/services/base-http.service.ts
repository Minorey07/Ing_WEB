import { Injectable } from '@angular/core';
import camelcaseKeys from 'camelcase-keys';
import snakecaseKeys from 'snakecase-keys';

const API_BASE = 'https://ing-web.onrender.com';

type CaseDirection = 'camel' | 'snake';

@Injectable({
  providedIn: 'root',
})
export class BaseHttpService {
  private transform(obj: any, direction: CaseDirection): any {
    if (!obj || typeof obj !== 'object') return obj;
    if (Array.isArray(obj)) return obj.map((item) => this.transform(item, direction));
    if (direction === 'snake') {
      return snakecaseKeys(obj, { deep: true });
    }
    return camelcaseKeys(obj, { deep: true });
  }

  private getToken(): string | null {
    const data = localStorage.getItem('usuario');
    if (!data) return null;
    try {
      const user = JSON.parse(data);
      return user.token || null;
    } catch {
      return null;
    }
  }

  private async request<T>(
    method: string,
    url: string,
    body?: any
  ): Promise<T> {
    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
    };

    const token = this.getToken();
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }

    const options: RequestInit = { method, headers };

    if (body !== undefined) {
      options.body = JSON.stringify(this.transform(body, 'snake'));
    }

    const response = await fetch(`${API_BASE}${url}`, options);
    const json = await response.json();

    if (!json.ok) {
      throw new Error(json.error || 'Error del servidor');
    }

    return this.transform(json.data, 'camel') as T;
  }

  async get<T>(url: string): Promise<T> {
    return this.request<T>('GET', url);
  }

  async post<T>(url: string, body: any): Promise<T> {
    return this.request<T>('POST', url, body);
  }

  async put<T>(url: string, body: any): Promise<T> {
    return this.request<T>('PUT', url, body);
  }

  async delete<T>(url: string): Promise<T> {
    return this.request<T>('DELETE', url);
  }
}
