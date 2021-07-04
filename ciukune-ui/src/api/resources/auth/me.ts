import { Resource } from '@ciukune/ckc'
import { getResource } from '@ciukune/ckc'
import { User } from '../../types/user'

export class MeResource extends Resource {
  state: User | undefined

  async refresh() {
    this.state  = await this._get<User>()
  }
}

export function getMeResource() : MeResource {
  return getResource(MeResource, 'auth/me')
}
