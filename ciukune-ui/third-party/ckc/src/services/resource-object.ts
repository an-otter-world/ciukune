import { Resource } from './resource'

export class ResourceObject<TObject> extends Resource {
  state: TObject | undefined = undefined;

  async load() {
    this.state = await this._get<TObject>()
  }

  async save() {
    await this._patch<void, TObject>(this.state)
  }

  async delete() {
    await this._delete()
  }
}
