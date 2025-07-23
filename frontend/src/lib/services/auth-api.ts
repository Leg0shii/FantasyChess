export class AuthAPIService {
    async register(username: string, password: string): Promise<void> {
        const response = await fetch(`${API_BASE}/auth/register`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        if (!response.ok) throw new Error('Registration failed');
        return response.json();
    }
    
    async login(username: string, password: string): Promise<string> {
        const response = await fetch(`${API_BASE}/auth/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        if (!response.ok) throw new Error('Login failed');
        const { token } = await response.json();
        localStorage.setItem('auth_token', token);
        return token;
    }

    async logout(): Promise<void> {
        localStorage.removeItem('auth_token');
    }

    isAuthenticated(): boolean {
        return !!localStorage.getItem('auth_token');
    }
}

export const authAPI: AuthAPIService = new AuthAPIService();