# $${\color{lightblue}Caching \space pattern}$$

Load data on demand into a cache from a data store. This pattern can improve performance and also helps to
maintain consistency between data held in the cache and the data in the underlying data store.

## Context & Problem
Applications use a cache to optimize repeated access to information held in a data store. However, it is usually impractical to expect that cached data will always be completely consistent with the data in the datastore. Applications should implement a strategy that helps to ensure that the data in the cache is up to date as far as possible, but can also detect and handle situations that arise when the data in the cache has become stale.

## Solution
Many commercial caching systems provide 
- read-through
    * An application retrieves data by referencing the cache. If the data is not in the cache, it is transparently retrieved from the data store and added to the cache.
- write-through/write-behind
    * An application retrieves data by referencing the cache. If the data is not in the cache, it is transparently retrieved from the data store and added to the cache. Any modifications to data held in the cache are automatically written back to the data store as well & vice versa.

## Considerations
- Lifetime of cache
- Evicting data
- Priming the cache
- Consistency
- Local (In memory) caching

## Use cases
- A cache does not provide native read-through and write-through operations.
- Resource demand is unpredictable. This pattern enables applications to load data on demand. It makes no assumptions about which data an application will require in advance.

*This pattern is not useful for following:*
- *When the cached data set is static. If the data will fit into the available cache space, prime the cache with the data on startup and apply a policy that prevents the data from expiring.*
- *For caching session state information in a web application hosted in a web farm. In this environment, you should avoid introducing dependencies based on client-server affinity*


## Example
    public class CacheService {
        private DataCache cache;
        private DatabaseService dbService;
        ...

        public DataItem getItemById(int id) {
            try
            {
                DataItem cacheItem = cache.getItemById(id);
                if(cacheItem != null)
                {
                    return cacheItem;
                }
                DataItem item = dbService.getItemById(id);
                cache.putItemById(id, item);
                return item;
            }
            catch(CacheServiceException ex)
            {
                ...
            }
        }
    }
### Author - Rahul Chaudhary