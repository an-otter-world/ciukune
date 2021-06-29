export interface MediaQueryOptions {
  breakpoints: Record<string, number>
}

export function mediaQuery(options?: MediaQueryOptions) : (query: string) => boolean {
  if(!options) {
    options = {
      breakpoints: {
        'sm': 576,
        'md': 768,
        'lg': 992,
        'xl': 1200,
        'xxl': 1400,
      }
    }
  }

  return (query: string) => true
}
